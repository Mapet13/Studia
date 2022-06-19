#include <iostream>
#include <cstring>
#include <cctype>
#include <charconv>

#include "fraction.h"

#if IMPLEMENTED_classFractionExists
#ifndef _MSC_FULL_VER // if not Visual Studio Compiler
    #warning "Klasa jest do zaimplementowania. Instrukcja w pliku naglowkowym"
#else
    #pragma message ("Klasa jest do zaimplementowania. Instrukcja w pliku naglowkowym")
#endif
#endif // IMPLEMENTED_classFractionExists

void Fraction::print() const
{
	save(std::cout);
	std::cout << '\n';
}

void Fraction::save(std::ostream& os) const
{
	os << numerator << '/' << denominator;
}

void Fraction::load(std::istream& is)
{
	std::string s;
	is >> s;

	const auto pos{ s.find_first_of('/') };
	std::from_chars(s.data(), s.data() + pos, numerator);
	std::from_chars(s.data() + pos + 1u, s.data() + s.size(), denominator);
}
