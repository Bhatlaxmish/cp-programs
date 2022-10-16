


#include <iostream>
#include<bits/stdc++.h>
using namespace std;

void createsuffix(int shift[], int borderpos[],
                  string pattern, int m)
{
    int i = m, j = m + 1;
    borderpos[i] = j;

    while (i > 0)
    {

        while (j <= m && pattern[i - 1] != pattern[j - 1])
        {

            if (shift[j] == 0)
            {
                shift[j] = j - i;
            }

            j = borderpos[j];
        }

        i--;
        j--;
        borderpos[i] = j;
    }
}

void makeitcorrect(int shift[], int borderpos[],
                   string pattern, int m)
{
    int i, j;
    j = borderpos[0];
    for (i = 0; i <= m; i++)
    {

        if (shift[i] == 0)
            shift[i] = j;

        if (i == j)
            j = borderpos[j];
    }
}

void search(string text, string pattern)
{
    int s = 0, j;
    int m = pattern.size();
    int n = text.size();

    int borderpos[m + 1], shift[m + 1];

    for (int i = 0; i < m + 1; i++)
        shift[i] = 0;

    createsuffix(shift, borderpos, pattern, m);
    makeitcorrect(shift, borderpos, pattern, m);

    while (s <= n - m)
    {

        j = m - 1;

        while (j >= 0 && pattern[j] == text[s + j])
            j--;

        if (j < 0)
        {
            cout << "pattern occurs at position " << s << "\n";
            s += shift[0];
        }
        else

            s += shift[j + 1];
    }
}

int main()
{
    string pattern, text;
    cin >> text >> pattern;
    search(text, pattern);
    return 0;
}
