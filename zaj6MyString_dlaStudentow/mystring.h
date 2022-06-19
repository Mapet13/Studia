#pragma once

#include <random>
#include <array>
#include <numeric>

class MyString 
{
	template<bool IsConst>
	struct iterator_t 
	{
		using base_type = std::conditional_t<IsConst, const MyString, MyString>;
		using iterator_category = std::random_access_iterator_tag;
		using difference_type = std::ptrdiff_t;
		using value_type = char;
		using pointer = value_type*;
		using reference = value_type&;

		explicit iterator_t(base_type* myString, std::size_t position)
			: m_ptr{ myString }, m_pos{ position }
		{}

		std::size_t getPosition() const { return m_pos; }
		
		template<bool C>
		bool operator==(iterator_t<C> anotherIt) const { return m_ptr == anotherIt.m_ptr && m_pos == anotherIt.m_pos; }
		
		template<bool C>
		bool operator!=(iterator_t<C> anotherIt) const { return !operator==(anotherIt); }
		
		iterator_t& operator++() { ++m_pos; return *this; }
		iterator_t& operator--() { --m_pos; return *this; }

		iterator_t operator+(std::size_t pos) { return iterator_t<IsConst>{ m_ptr, m_pos + pos }; }
		
		template<bool C>
		std::size_t operator-(iterator_t<C> anotherIt) const { return m_pos - anotherIt.m_pos; }
		
		template <bool Q = IsConst>
		typename std::enable_if_t<Q, value_type> operator*() const { return (*m_ptr)[m_pos]; }

		template <bool Q = IsConst>
		typename std::enable_if_t<!Q, reference> operator*() { return (*m_ptr)[m_pos]; }
	private:
		base_type* m_ptr;
		std::size_t m_pos;
	};

public:
	using iterator = iterator_t<false>;
	using const_iterator = iterator_t<true>;

	MyString() = default;
	MyString(const char* text) {
		std::string_view t_sv{ text };
		m_size =  t_sv.size();

		copyToInitial(t_sv);

		if (m_size > initialBufferSize)
			copyToAdditional(t_sv);
	}
	MyString(const MyString& text) {
		for (const auto c : text)
			push_back(c);
	}
	
	explicit operator std::string() const {
		std::string result;
		result += m_inititial_buffer;
		if (m_size > initialBufferSize)
			result += m_additional_buffer;
		return result;
	}
	
	std::size_t capacity() const { return initialBufferSize + m_additional_buffer.capacity(); }
	bool empty() const { return m_size == 0; }
	std::size_t size() const { return m_size; }
	
	iterator begin() { return iterator(this, 0); }
	iterator end() { return iterator(this, m_size); }
	
	const_iterator begin() const { return const_iterator(this, 0); }
	const_iterator end() const { return const_iterator(this, m_size); }
	
	const_iterator cbegin() const { return const_iterator(this, 0); }
	const_iterator cend() const { return const_iterator(this, m_size); }

	bool operator!=(const MyString& rhs) const { return !operator==(rhs); }
	bool operator==(const MyString& rhs) const { 
		if (rhs.size() != m_size) return false;
		return std::all_of(begin(), end(), [i = 0, &rhs](const auto c) mutable {
			return c == rhs[i++];
		});
	}
	bool operator<(const MyString& rhs) const {
		return std::lexicographical_compare(begin(), end(), std::begin(rhs), std::end(rhs));
	}

	char operator[](std::size_t pos) const { 
		if (pos >= m_size) throw std::out_of_range("out of range");
		return pos < initialBufferSize ? m_inititial_buffer[pos] : m_additional_buffer[pos - initialBufferSize]; 
	}
	char& operator[](std::size_t pos) { 
		if (pos >= m_size) throw std::out_of_range("out of range");
		return pos < initialBufferSize ? m_inititial_buffer[pos] : m_additional_buffer[pos - initialBufferSize]; 
	}

	void operator+=(const char c) { push_back(c); }

	friend std::ostream& operator<< (std::ostream& stream, const MyString& str) { 
		for (const auto it : str) {
			stream << it;
		}
		return stream; 
	}
	friend std::istream& operator>> (std::istream& stream, MyString& str) { 
		std::for_each(std::istreambuf_iterator<char>{stream}, std::istreambuf_iterator<char>(), [&str](const auto c) {
			str.push_back(c);
		});
		return stream; 
	}
	
	void push_back(char c) {
		if (m_size >= initialBufferSize)
			m_additional_buffer += c;
		else
			m_inititial_buffer[m_size] = c;

		++m_size;
	}

	void clear() {
		m_additional_buffer.clear();
		m_size = 0;
	}

	std::map<MyString, std::size_t> countWordsUsageIgnoringCases() const { return {}; }
	bool all_of(std::function<bool(char)> predicate) const { return std::all_of(begin(), end(), predicate); }
	std::set<MyString> getUniqueWords() const { return {}; }
	
	MyString join(const std::vector<MyString>& texts) const { 
		MyString result;

		bool isFirst{ true };
		for (const auto& str : texts) {
			if (!isFirst) {
				result.push_back(',');
				result.push_back(' ');
			}
			isFirst = false;
			for (const auto c : str) {
				result.push_back(c);
			}
		}

		return result;
	}
	
	bool startsWith(const char* text) const {
		std::string_view sv{ text };
		
		return (m_size >= sv.size()) && std::all_of(std::begin(sv), std::end(sv), [i = 0, this](const auto c) mutable {
			return c == operator[](i++);
		});
	}
	
	MyString& toLower() { 
		for (auto& c : *this) {
			c = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
		}
		return *this; 
	}
	
	MyString& trim() { 
		return *this;
	}
	
	bool endsWith(const char* text) const {
		std::string_view sv{ text };
		return (m_size >= sv.size()) && std::all_of(std::rbegin(sv), std::rend(sv), [i = (m_size-1), this](const auto c) mutable {
			return c == operator[](i--);
		});
	}
	

	static MyString generateRandomWord(std::size_t length) { 
		std::random_device rd;
		std::mt19937 gen(rd());
		std::uniform_int_distribution<int> dist('a', 'z');

		MyString str{};

		for (auto i{ 0u }; i < length; ++i) {
			str.push_back(static_cast<char>(dist(gen)));
		}

		return str;
	}

	static constexpr std::size_t initialBufferSize{ 20 };
private:
	void copyToInitial(std::string_view text) {
		const auto initial_size = std::min(text.size(), initialBufferSize);
		std::generate_n(std::begin(m_inititial_buffer), initial_size, [text, i = 0u]() mutable {
			return text[i++];
		});
	}

	void copyToAdditional(std::string_view text) {
		m_additional_buffer = text.substr(initialBufferSize);
	}

	std::size_t m_size{ 0 };
	char m_inititial_buffer[initialBufferSize]{ '\0' };
	std::string m_additional_buffer{ "" };
};