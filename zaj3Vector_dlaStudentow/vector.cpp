// author: Grzegorz Prowadzacy

#include "vector.h"

#include <algorithm>
#include <stdexcept>
#include <utility>  // std::swap()

Vector::Vector(const std::size_t capacity) : capacity_(capacity) {}

Vector::Vector(Vector&& other) noexcept {
    std::swap(capacity_, other.capacity_);
    std::swap(size_, other.size_);
    data_ = std::unique_ptr<Fraction[]>(new Fraction[other.capacity_]);
    std::copy_n(other.data_.get(), size_, data());
}

Vector& Vector::operator=(const Vector& other) noexcept {
    capacity_ = other.capacity_;
    size_ = other.size_;
    data_ = std::unique_ptr<Fraction[]>(new Fraction[other.capacity_]);
    std::copy_n(other.data_.get(), size_, data());
    return *this;
}

Vector& Vector::operator=(Vector&& other) noexcept {
    std::swap(capacity_, other.capacity_);
    std::swap(size_, other.size_);
    data_ = std::move(other.data_);
    return *this;
}

std::size_t Vector::size() const noexcept {
    return size_;
}

std::size_t Vector::capacity() const noexcept {
    return capacity_;
}

Fraction* Vector::data() noexcept {
    return data_.get();
}

void Vector::push_back(const Fraction obj) {
    if (size_ >= capacity_) {
        ++capacity_;
        std::unique_ptr<Fraction[]> new_data{ new Fraction[capacity_] };
        std::copy_n(data(), size_, new_data.get());
        data_ = std::move(new_data);
    }
    data_[size_] = obj;
    ++size_;
}

Fraction& Vector::operator[](const std::size_t index) {
    if (index >= size_)
        throw std::out_of_range("inxex > vector size!");
    return data()[index];
}

const Fraction& Vector::operator[](const std::size_t index) const {
    if (index >= size_)
        throw std::out_of_range("inxex > vector size!");
    return data_.get()[index];
}

Vector::Vector(const Vector& other) : capacity_(other.capacity_),
                                      size_(other.size_) {
    std::copy_n(other.data_.get(), size_, data());
}
