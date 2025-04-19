#include <iostream>
using namespace std;

long long countVanSubsequence(std::string s) {
    long long v = 0, va = 0, van = 0;
    for (char c : s) {
        if (c == 'v') {
            v++;
        } else if (c == 'a') {
            va += v;
        } else if (c == 'n') {
            van += va;
        }
    }
    return van;
}

int main()
{
    int n, m, x;
    std::cin >> n >> m;
    std::string s;
    // char c;
    std::cin >> s;
    for (int i = 1; i <= m; i++)
    {
        std::cin >> x;
        if (x >= n)
        {
            continue;
        }
        swap(s[x - 1], s[x]);
        // c = s[x];
        // s[x] = s[x + 1];
        // s[x + 1] = c;
        std::cout << countVanSubsequence(s) << std::endl;
        // std::cout << s << std::endl;
    }
    return 0;
}