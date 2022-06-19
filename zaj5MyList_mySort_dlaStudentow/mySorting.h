#pragma once

#include "myList.h"

template<typename T>
void mySort(T& contener) {
	std::sort(std::begin(contener), std::end(contener));
}

template <std::size_t M, std::size_t N>
void mySort(char (&contener)[M][N])
{
    const auto shouldBeSwaped = [](const std::string_view x, const std::string_view y) {
        return !std::lexicographical_compare(std::begin(x), std::end(x), std::begin(y), std::end(y), [](const auto a, const auto b) {
            return std::tolower(a) < std::tolower(b);
            });
    };

    for (auto i = 0u; i < M; ++i) {
        for (auto j = 0u; j < M - 1; ++j) {
            if (shouldBeSwaped(contener[j], contener[j + 1]))
                std::swap(contener[j], contener[j + 1]);
        }
    }
}

template<typename T>
void mySort(MyList<T>& list) {
    auto safe_next = [](auto node) {
        return node && node->next ? node->next.get() : nullptr;
    };

    auto temp = list.head->next.get();

    while (temp != nullptr) {
        auto min = temp;
        auto node = temp->next.get();

        while (node != nullptr) {
            if (min->value > node->value)
                min = node;


            node = safe_next(node);
        }

        std::swap(temp->value, min->value);
        temp = safe_next(temp);
    }
}

