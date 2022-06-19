#include <gsl/gsl_linalg.h>

#include <algorithm>
#include <charconv>
#include <chrono>
#include <cmath>
#include <concepts>
#include <iostream>
#include <optional>
#include <random>
#include <ranges>
#include <vector>

namespace utils {
    template <typename T>
    concept numeric_type = (std::integral<T> || std::floating_point<T>)&&!std::same_as<bool, T> && requires(T param) {
        requires std::is_arithmetic_v<decltype(param + 1)>;
        requires !std::is_pointer_v<T>;
    };

    template <typename T, typename Stream>
    concept streamable = requires(T t, Stream stream) {
        { stream << t };
    };

    template <std::floating_point T, std::floating_point auto MIN, std::floating_point auto MAX>
    class RandomGenarator {
        std::uniform_real_distribution<T> _distr{ MIN, MAX };
        std::random_device _device;
        std::mt19937 _engine{ _device() };

       public:
        [[nodiscard]] auto next() { return _distr(_engine); }
    };

    template <std::ranges::range T>
    constexpr auto enumerate(T&& iterable) {
        class iterator {
            std::ranges::range_difference_t<T> i{};
            std::ranges::iterator_t<T> iter;

           public:
            iterator(std::ranges::iterator_t<T> it) : iter(std::move(it)) {}

            bool operator!=(const iterator& other) const {
                return iter != other.iter;
            }

            void operator++() {
                ++i;
                ++iter;
            }

            auto operator*() const {
                return std::tie(i, *iter);
            }
        };
        struct iterable_wrapper {
            T iterable;
            auto begin() {
                return iterator(std::begin(iterable));
            }
            auto end() {
                return iterator(std::end(iterable));
            }
        };
        return iterable_wrapper{ std::forward<T>(iterable) };
    }

    template <numeric_type T>
    auto get_num_input(std::string_view input) {
        T result{};
        const auto [ptr, ec] = std::from_chars(input.data(), input.data() + input.size(), result);

        return ec == std::errc() ? std::optional{ result } : std::nullopt;
    };
}  // namespace utils

template <double MIN, double MAX>
auto generate_vector(std::size_t n, utils::RandomGenarator<double, MIN, MAX>& rand_generator) {
    std::vector<double> vec(n);
    std::ranges::generate(vec, [&rand_generator]() { return rand_generator.next(); });
    return vec;
}

template <double MIN, double MAX>
std::tuple<std::vector<double>, std::vector<double>> generate_data(std::size_t n) {
    utils::RandomGenarator<double, MIN, MAX> rand_genarator;
    return std::tuple{ generate_vector<MIN, MAX>(n * n, rand_genarator), generate_vector(n, rand_genarator) };
}

template <typename VecType>
requires requires(VecType vec, std::size_t index) {
    { vec[index] } -> utils::streamable<decltype(std::cout)>;
}
auto print_vec(std::size_t n, const VecType& vec, std::string_view label) -> void {
    std::cout << label << ":[";
    for (std::size_t i = 0; i < n; ++i) {
        std::cout << vec[i] << ' ';
    }
    std::cout << "]\n";
}

void print_equation(std::size_t n, const std::vector<double>& matrix, const std::vector<double>& vec, const double* result) {
    std::cout << "Matrix:\n|";
    for (const auto [i, x]: utils::enumerate(matrix)) {
        if (i % n == 0 && i != 0)
            std::cout << "|\n|";
        std::cout.width(10);
        std::cout << x << ' ';
    }
    std::cout << "|\n\n";

    print_vec(n, vec, "Vector");
    print_vec(n, result, "X");
}

void check_if_solution_is_corrct(std::size_t n, const std::vector<double>& vec, const gsl_matrix& test) {
    print_vec(n, test.data, "Multiplied");

    print_vec(n, (std::views::iota(0) | std::views::take(n) | std::views::transform([&vec, &test](const auto& i) {
                      return std::abs(vec[i] - test.data[i]);
                  })),
              "Errors");
}

auto solve_lu(std::size_t n, std::vector<double> matrix, std::vector<double> vec) -> std::chrono::nanoseconds {
    const std::vector<double> matrix_cpy(matrix);

    const auto time_start = std::chrono::steady_clock::now();

    auto matrix_view{ gsl_matrix_view_array(matrix.data(), n, n) };
    const auto vec_view{ gsl_vector_view_array(vec.data(), n) };

    auto* result = gsl_vector_alloc(n);
    auto* permutation = gsl_permutation_alloc(n);

    int signum;
    gsl_linalg_LU_decomp(&matrix_view.matrix, permutation, &signum);
    gsl_linalg_LU_solve(&matrix_view.matrix, permutation, &vec_view.vector, result);

    const auto time_end = std::chrono::steady_clock::now();

    print_equation(n, matrix_cpy, vec, result->data);

    const auto result_view{ gsl_matrix_view_array(result->data, n, 1) };
    const auto matrix_cpy_view{ gsl_matrix_view_array(result->data, n, n) };
    auto test = gsl_matrix_alloc(n, 1);
    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, &matrix_cpy_view.matrix, &result_view.matrix, 0.0, test);

    check_if_solution_is_corrct(n, vec, *test);

    gsl_permutation_free(permutation);
    gsl_vector_free(result);
    gsl_matrix_free(test);

    return std::chrono::duration_cast<std::chrono::nanoseconds>(time_end - time_start);
}

auto solve_qr(std::size_t n, std::vector<double>&& matrix, std::vector<double>&& vec) -> std::chrono::nanoseconds {
    const std::vector<double> matrix_cpy(matrix);

    const auto time_start = std::chrono::steady_clock::now();

    auto matrix_view{ gsl_matrix_view_array(matrix.data(), n, n) };
    const auto vec_view{ gsl_vector_view_array(vec.data(), n) };

    auto* result = gsl_vector_alloc(n);
    auto* tau = gsl_vector_alloc(n);

    gsl_linalg_QR_decomp(&matrix_view.matrix, tau);
    gsl_linalg_QR_solve(&matrix_view.matrix, tau, &vec_view.vector, result);

    const auto time_end = std::chrono::steady_clock::now();

    print_equation(n, matrix_cpy, vec, result->data);

    const auto matrix_cpy_view{ gsl_matrix_view_array(result->data, n, n) };
    const auto result_view{ gsl_matrix_view_array(result->data, n, 1) };
    auto test = gsl_matrix_alloc(n, 1);
    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, &matrix_cpy_view.matrix, &result_view.matrix, 0.0, test);

    check_if_solution_is_corrct(n, vec, *test);

    gsl_vector_free(tau);
    gsl_vector_free(result);
    gsl_matrix_free(test);

    return std::chrono::duration_cast<std::chrono::nanoseconds>(time_end - time_start);
}

auto solve_invert(std::size_t n, std::vector<double>&& matrix, std::vector<double>&& vec) -> std::chrono::nanoseconds {
    const std::vector<double> matrix_cpy(matrix);

    const auto time_start = std::chrono::steady_clock::now();

    auto matrix_view{ gsl_matrix_view_array(matrix.data(), n, n) };
    const auto vec_view{ gsl_matrix_view_array(vec.data(), n, 1) };

    auto* invert = gsl_matrix_alloc(n, n);
    auto* result = gsl_matrix_alloc(n, 1);
    auto* permutation = gsl_permutation_alloc(n);
    int signum;
    gsl_linalg_LU_decomp(&matrix_view.matrix, permutation, &signum);
    gsl_linalg_LU_invert(&matrix_view.matrix, permutation, invert);
    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, invert, &vec_view.matrix, 0.0, result);

    const auto time_end = std::chrono::steady_clock::now();

    print_equation(n, matrix_cpy, vec, result->data);

    auto test = gsl_matrix_alloc(n, 1);
    const auto matrix_cpy_view{ gsl_matrix_view_array(result->data, n, n) };
    gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1.0, &matrix_cpy_view.matrix, result, 0.0, test);

    check_if_solution_is_corrct(n, vec, *test);

    gsl_permutation_free(permutation);
    gsl_matrix_free(result);
    gsl_matrix_free(test);
    gsl_matrix_free(invert);

    return std::chrono::duration_cast<std::chrono::nanoseconds>(time_end - time_start);
}

void solve_with(std::size_t n, std::invocable<std::size_t, std::vector<double>, std::vector<double>> auto solver) {
    static constexpr auto MIN{ 0.0 };
    static constexpr auto MAX{ 1.0 };

    auto [matrix, vec]{ generate_data<MIN, MAX>(n) };

    const auto time = solver(n, std::move(matrix), std::move(vec));
    std::cout << "\n\nTime: " << time.count() << "ns\n";
}

int main(int argc, char** argv) {
    if (argc == 2) {
        if (const auto parsed_input{ utils::get_num_input<std::size_t>(argv[1]) }; parsed_input.has_value()) {
            std::cout << "-------------------------------------------------------\n";
            std::cout << "QR:\n";
            solve_with(parsed_input.value(), solve_qr);
            std::cout << "-------------------------------------------------------\n";
            std::cout << "LU:\n";
            solve_with(parsed_input.value(), solve_lu);
            std::cout << "-------------------------------------------------------\n";
            std::cout << "INVERT:\n";
            solve_with(parsed_input.value(), solve_invert);
            std::cout << "-------------------------------------------------------\n";

            return 0;
        }
    }

    std::cout << "To use: [" << argv[0] << "N] where N matrix size\n";
    return 1;
}
