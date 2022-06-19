#include "matrix.h"

#include <charconv>
#include <iostream>
#include <string>

#ifndef _MSC_FULL_VER  // if not Visual Studio Compiler
#warning "Klasa jest do zaimplementowania. Instrukcja w pliku naglowkowym"
#else
#pragma message("Klasa jest do zaimplementowania. Instrukcja w pliku naglowkowym")
#endif

TwoDimensionMatrix operator+(const TwoDimensionMatrix& matrix1, const TwoDimensionMatrix& matrix2) {
    TwoDimensionMatrix result{ matrix1.matrix };
    result.for_each([&matrix2](auto& elem, const auto x, const auto y) { elem += matrix2.matrix[x][y]; });
    return result;
}

std::istream& operator>>(std::istream& is, TwoDimensionMatrix& matrix) {
    static constexpr auto second_num_offset = 1;

    std::string line;
    for (size_t y = 0; y < matrix.getSize(); ++y) {
        std::getline(is, line);

        const auto [fisrt_num_end, _]{ std::from_chars(line.data(), line.data() + line.size(), matrix[y][0]) };
        std::from_chars(fisrt_num_end + second_num_offset, line.data() + line.size(), matrix[y][1]);
    }

    return is;
}

std::ostream& operator<<(std::ostream& out, const TwoDimensionMatrix& matrix) {
    matrix.for_each([&out](const auto& elem) { out << elem << ','; });
    return out;
}

TwoDimensionMatrix::TwoDimensionMatrix() {
    for_each([](MatrixElement& elem) { elem = 0; });
}

TwoDimensionMatrix::TwoDimensionMatrix(const MatrixElement arr[size][size]) {
    std::copy(&arr[0][0], &arr[0][0] + size * size, &matrix[0][0]);
}

TwoDimensionMatrix& TwoDimensionMatrix::operator=(TwoDimensionMatrix other) {
    std::swap(other.matrix, matrix);
    return *this;
}

TwoDimensionMatrix& TwoDimensionMatrix::operator*=(MatrixElement number) {
    for_each([number](MatrixElement& elem) { elem *= number; });
    return *this;
}

TwoDimensionMatrix TwoDimensionMatrix::operator&&(const TwoDimensionMatrix& other) const {
    TwoDimensionMatrix result{ matrix };
    result.for_each([&other](auto& elem, const auto x, const auto y) { elem = elem && other.matrix[x][y]; });
    return result;
}

// helpers ---------------------------------------------------------------------------------
void TwoDimensionMatrix::for_each(std::function<void(MatrixElement&)> function) {
    for (auto& arr: matrix)
        for (auto& elem: arr)
            function(elem);
}
void TwoDimensionMatrix::for_each(std::function<void(const MatrixElement&)> function) const {
    for (const auto& arr: matrix)
        for (const auto& elem: arr)
            function(elem);
}
void TwoDimensionMatrix::for_each(std::function<void(MatrixElement&, size_t x, size_t y)> function) {
    for (size_t x = 0; x < size; ++x)
        for (size_t y = 0; y < size; ++y)
            function(matrix[x][y], x, y);
}
//---------------------------------------------------------------------------------
