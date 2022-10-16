#include <bits/stdc++.h>

using namespace std;

class obj

{

public:
    string skill_name;

    int level;
};

class pro

{

public:
    int days;

    int score;

    int bestScore;

    int numberOfroles;

    vector<obj> skills;
};

int main()

{

    int number_contributors, number_projects;

    ifstream fin("student0.txt", ios::in);

    ofstream fout("output.txt", ios::out);

    fin >> number_contributors >> number_projects;

    unordered_map<string, vector<obj>> mp;

    unordered_map<string, pro> mp2;

    for (int i = 0; i < number_contributors; i++)

    {

        string temp;

        fin >> temp;

        int temp2;

        fin >> temp2;

        vector<obj> temp3;

        obj ob;

        for (int i = 0; i < temp2; i++)

        {

            fin >> ob.skill_name >> ob.level;

            temp3.push_back(ob);
        }

        mp[temp] = temp3;
    }

    for (int i = 0; i < number_projects; i++)

    {

        pro pr;

        string temp;

        fin >> temp;

        fin >> pr.days >> pr.score >> pr.bestScore >> pr.numberOfroles;

        vector<obj> temp1;

        for (int j = 0; j < pr.numberOfroles; j++)

        {

            obj ob;

            fin >> ob.skill_name >> ob.level;

            temp1.push_back(ob);
        }

        pr.skills = temp1;

        mp2[temp] = pr;
    }

    // first one by one project

    // a skill iro person assign

    unordered_map<string, vector<string>> finans;

    unordered_map<string, int> check;

    bool is = 0;

    for (auto project : mp2)

    {

        vector<string> temp;

        for (auto required : project.second.skills)

        {

            is = 0;

            for (auto contributor : mp)

            {

                for (auto skill : contributor.second)

                {

                    if (skill.skill_name == required.skill_name && skill.level >= required.level)

                    {

                        int check = 0;

                        for (auto m : temp)

                        {

                            if (m == contributor.first)

                            {

                                check = 1;

                                break;
                            }
                        }

                        if (check == 0)

                        {

                            temp.push_back(contributor.first);

                            is = 1;

                            break;
                        }
                    }

                    else if (skill.skill_name == required.skill_name && skill.level + 1 == required.level)

                    {

                        for (auto m : temp)

                        {

                            for (auto x : mp[m])

                            {

                                if (x.skill_name == required.skill_name && x.level >= required.level)

                                {

                                    int check = 0;

                                    for (auto l : temp)

                                    {

                                        if (l == contributor.first)

                                        {

                                            check = 1;

                                            break;
                                        }
                                    }

                                    if (check == 0)

                                    {

                                        temp.push_back(contributor.first);

                                        is = 1;

                                        break;
                                    }
                                }
                            }
                        }
                    }
                }

                if (is)

                {

                    break;
                }
            }
        }

        finans[project.first] = temp;
    }

    int count = 0;

    for (auto x : finans)

    {

        if (x.second.size() == mp2[x.first].numberOfroles)

        {

            count++;
        }
    }

    fout << count << "\n";

    for (auto x : finans)

    {

        if (x.second.size() == mp2[x.first].numberOfroles)

        {

            fout << x.first << "\n";

            for (auto y : x.second)

            {

                fout << y << " ";
            }

            fout << "\n";
        }
    }
}