#include "fraction.h"

#include <numeric>
#include <stdexcept>

Fraction::Fraction(int numerator, int denominator) : numerator_(numerator) {
    setDenominator(denominator);
}

void Fraction::setNumerator(int numerator) noexcept { numerator_ = numerator; }

void Fraction::setDenominator(int denominator) {
    if (denominator == invalid_denominator_value)
        throw std::invalid_argument{ "Invalid denominator value" };

    denominator_ = denominator;
}

Fraction Fraction::getReduced() const noexcept {
    const auto gcd = std::gcd(numerator_, denominator_);
    return Fraction(numerator_ / gcd, denominator_ / gcd);
}

Fraction Fraction::operator+(const Fraction& obj) const {
    return Fraction{ (numerator_ * obj.denominator()) + (obj.numerator() * denominator_), denominator_ * obj.denominator() }.getReduced();
}

Fraction Fraction::operator*(const Fraction& obj) const {
    return Fraction{ numerator_ * obj.numerator(), denominator_ * obj.denominator() }.getReduced();
}
