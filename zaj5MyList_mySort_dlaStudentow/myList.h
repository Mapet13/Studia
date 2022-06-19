#pragma once

#include <exception>
#include <memory>

template<typename T>
class MyList {
public:
	struct Node {
		Node(std::unique_ptr<Node> next, T value) : next(std::move(next)), value(std::move(value)) {}

		std::unique_ptr<Node> next;
		T value;
	};

	template<bool IsConst>
	struct iterator_t {
		using iterator_category = std::forward_iterator_tag;
		using difference_type = std::ptrdiff_t;
		using value_type = T;
		using pointer = value_type*;
		using reference = value_type&;

		iterator_t(Node* ptr) : m_ptr(ptr) {}
		iterator_t& operator++();
		iterator_t operator++(int n);
		template <bool Q = IsConst>
		typename std::enable_if<Q, const T&>::type operator*() { return m_ptr->value; }
		template <bool Q = IsConst>
		typename std::enable_if<!Q, T&>::type operator*() { return m_ptr->value; }
		bool operator==(const iterator_t& iter) { return m_ptr == iter.m_ptr; }
		bool operator!=(const iterator_t& iter) { return !operator==(iter); }

	private:
		Node* m_ptr;
	};


	using value_type = T;
	using difference_type = std::size_t;
	using pointer = T*;
	using reference = T&;
	using iterator = iterator_t<false>;
	using const_iterator = iterator_t<true>;


	MyList() = default;
	MyList(const MyList&) = delete;
	MyList& operator=(MyList) = delete;

	std::size_t size() const noexcept { return m_size; }

	iterator begin() noexcept { return iterator{ head->next.get() }; }
	const_iterator begin() const noexcept { return const_iterator{ head->next.get() }; }
	iterator end() noexcept { return iterator{ nullptr }; }
	const_iterator end() const noexcept { return const_iterator{ nullptr }; }

	void push_front(const T& new_value);

	T pop_front();

	T& front();

	void remove(T value);

	friend std::ostream& operator<< (std::ostream& stream, const MyList<T>& list) {
		for (const auto& x : list) stream << x << ',';
		return stream;
	}

public:
	std::unique_ptr<Node> head = std::make_unique<Node>(nullptr, T());
private:
	std::size_t m_size{ 0 };
};

template<typename T>
void MyList<T>::push_front(const T& new_value) {
	auto new_node = std::make_unique<Node>(std::move(head->next), new_value);
	head->next = std::move(new_node);

	++m_size;
}

template<typename T>
T MyList<T>::pop_front() {
	if (m_size == 0)
		throw std::out_of_range("empty list");

	auto value = std::move(head->next->value);
	head->next = std::move(head->next->next);

	--m_size;

	return value;
}

template<typename T>
T& MyList<T>::front() {
	if (m_size == 0)
		throw std::out_of_range("empty list");

	return head->next->value;
}

template<typename T>
void MyList<T>::remove(T value) {
	auto* it = head.get();
	while (it->next != nullptr) {
		if (it->next->value == value) {
			it->next = std::move(it->next->next);
			--m_size;
		}
		else it = it->next.get();
	}
}

template<typename T>
template<bool IsConst>
MyList<T>::iterator_t<IsConst>& MyList<T>::iterator_t<IsConst>::operator++() { 
	m_ptr = m_ptr->next.get(); 
	return *this; 
}

template<typename T>
template<bool IsConst>
MyList<T>::iterator_t<IsConst> MyList<T>::iterator_t<IsConst>::operator++(int n) {
	MyList<T>::iterator_t<IsConst> result(m_ptr);
	for (auto i = 0u; i < n; ++i) m_ptr = m_ptr->next.get();
	return result;
}