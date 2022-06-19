#include <cmath>
#include <iostream>
#include <random>
#include <ranges>
#include <utility>
#include <array>

#include <gsl/gsl_math.h>
#include <gsl/gsl_monte.h>
#include <gsl/gsl_monte_plain.h>
#include <gsl/gsl_monte_miser.h>
#include <gsl/gsl_monte_vegas.h>


static constexpr auto MIN{ 0.0 };
static constexpr auto MAX{ 1.0 };
static constexpr auto MAX_AREA{ 1.0 };
static constexpr std::array tested_values{ 10u, 50u, 100u, 5000u, 400000u };

double f1(double x) { return x * x; }
double f2(double x) { return 1.0 / std::sqrt(x); }

auto hit_and_miss(std::size_t N, auto function)
{
	std::random_device rd; 
	std::mt19937 gen(rd());
	const std::uniform_real_distribution dis(MIN, MAX);

	const double hited_count = std::ranges::count_if(
		std::views::iota(0)
			| std::views::transform([&dis, &gen](const auto i) 
			{
					return std::pair{dis(gen), dis(gen)};
			})
			| std::views::take(N)
		, [function](const auto point)
	{
		const auto [x, y] = point;
		return y <= function(x);
	});

	return MAX_AREA * (hited_count / static_cast<double>(N));
}

auto f1_monte(double x[], size_t dim, void* p) {
	return f1(x[0]);
}

auto f2_monte(double x[], size_t dim, void* p) {
	return f2(x[0]);
}


auto gsl_method(auto* f)
{
	static constexpr double xl[1] = { MIN };
	static constexpr double xu[1] = { MAX };
	static constexpr auto calls = 2000;

	// ------------ GSL START ------------
	gsl_monte_function F;
	F.f = f;
	F.dim = 1;
	F.params = NULL;

	double res, err;
	const gsl_rng_type* T;
	gsl_rng* r;
	gsl_rng_env_setup();
	T = gsl_rng_default;
	r = gsl_rng_alloc(T);

	gsl_monte_plain_state* s = gsl_monte_plain_alloc(1);
	gsl_monte_plain_integrate(&F, xl, xu, 1, calls, r, s,
		&res, &err);
	gsl_monte_plain_free(s);
	// ------------ GSL END ------------

	return std::pair{ res, err};
}

auto calculate_monte_carlo(std::string_view label, auto f) {
	const auto [res, err] = gsl_method(f);
	std::cout << label << ": err = " << err << "; res = " << res << '\n';
}

int main()
{
	////////////////////////////////////////////////////////////
	std::cout << "hit_and_miss\n\n";
	std::cout << "x^2:\n";
	for(const auto N : tested_values)
	{
		std::cout << "For " << N << " point -> " << hit_and_miss(N, f1) << '\n';
	}
	std::cout << "\n\n1/sqrt(x):\n";
	for (const auto N : tested_values)
	{
		std::cout << "For " << N << " point -> " << hit_and_miss(N, f2) << '\n';
	}
	//////////////////////////////////////////////////////////////

	std::cout << "\n\n\ngsl:\n";

	calculate_monte_carlo("x^2", f1_monte);
	calculate_monte_carlo("1/sqrt(x)", f2_monte);
}
