/*

算法相关的主文件，用于统一调用所有算法功能

g++ -o .\algorithm .\algorithm.cpp -std=c++17

.\algorithm

*/

// 考虑到部分编译器没有bits/stdc++.h，所以加到了/src/header/stdc++.h中
#define bits / stdc++.h header / stdc++.h

#include "bits/stdc++.h"
#include <numeric> // for std::gcd and std::lcm (C++17)
#include <chrono>

// #include "header/stdc++.h"

class Find_GCD_LCM
{
    /*
     * 求最大公约数和最小公倍数
     */
public:
    void get_gcd(std::string input_file, std::string output_file, std::string segmentation = "\n")
    {
        freopen(input_file.c_str(), "r", stdin);
        freopen(output_file.c_str(), "w", stdout);
        long long a, b;
        while (true)
        {
            scanf("%lld", &a);
            if (a < 0)
            {
                return;
            }
            scanf("%lld", &b);
            if (b < 0)
            {
                return;
            }
            printf("%lld%s", std::gcd(a, b), segmentation);
        }
        fclose(stdin);
        fclose(stdout);
    }
    void get_lcm(std::string input_file, std::string output_file, std::string segmentation = "\n")
    {
        freopen(input_file.c_str(), "r", stdin);
        freopen(output_file.c_str(), "w", stdout);
        long long a, b;
        while (true)
        {
            scanf("%lld", &a);
            if (a < 0)
            {
                return;
            }
            scanf("%lld", &b);
            if (b < 0)
            {
                return;
            }
        }
        printf("%lld%s", std::lcm(a, b), segmentation);
        fclose(stdin);
        fclose(stdout);
    }
    void get_all(std::string input_file, std::string output_file)
    {
        freopen(input_file.c_str(), "r", stdin);
        freopen(output_file.c_str(), "w", stdout);
        putchar('g'), putchar('c'), putchar('d'), putchar(' '), putchar('|'), putchar(' ');
        putchar('l'), putchar('c'), putchar('m'), putchar('\n');
        long long a, b;
        while (true)
        {
            scanf("%lld", &a);
            if (a < 0)
            {
                return;
            }
            scanf("%lld", &b);
            if (b < 0)
            {
                return;
            }
            printf("%lld %lld\n", std::gcd(a, b), std::lcm(a, b));
        }
        fclose(stdin);
        fclose(stdout);
    }
};

int main(int argc, char *argv[])
{
    // std::cout << "Hello World!" << std::endl;
    // auto start = std::chrono::high_resolution_clock::now();
    Find_GCD_LCM gcd_lcm;
    gcd_lcm.get_all("input.in", "output.out");
    // auto end = std::chrono::high_resolution_clock::now();

    // // 计算时间差（毫秒）
    // auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    // std::cout << "耗时: " << duration.count() << " 毫秒" << std::endl;
    return 0;
}