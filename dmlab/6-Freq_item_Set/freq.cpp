#include <bits/stdc++.h>
using namespace std;

map<int, vector<vector<string>>> itemsets;

vector<set<string>> trs; // Transactions
double min_supp, min_conf;
int sc;

// Generating all possible subsets/itemsets

void generateItemSets(vector<string> &items, vector<string> curr, int idx)
{

    if (idx == items.size())
    {
        int s = curr.size();

        itemsets[s].push_back(curr); // Size : itemsetS of given size
        return;
    }

    generateItemSets(items, curr, idx + 1);
    curr.push_back(items[idx]);
    generateItemSets(items, curr, idx + 1);
}

// Tells in how many transactions given
int countTrs(vector<string> is)
{

    int count = 0;

    // For each transaction
    for (auto t : trs)
    {
        bool found = true;

        // Check if all items of given itemset are present or not
        for (auto it : is)
        {
            if (t.find(it) == t.end())
            {
                found = false;
                break;
            }
        }

        count += found == true; // Increase count if all items of given itemset were present in the tranaction
    }

    return count;
}

vector<vector<string>> calcFreqItemSet(int size)
{

    vector<vector<string>> freqIt;

    for (auto v : itemsets[size])
    {
        int count = countTrs(v); // COunt the number of transaction in which itemset v is present

        if (count >= sc)
            freqIt.push_back(v); // Add in frequent itemset if count>=min_supprt_count
    }

    return freqIt;
}

void generateAssociationRule(vector<string> itemset, int idx, vector<string> v1, vector<string> v2)
{

    if (idx == itemset.size())
    {

        if (v1.size() == 0 || v2.size() == 0)
            return;

        int cnt = countTrs(itemset);
        int cnt1 = countTrs(v1);
        int cnt2 = countTrs(v2);
        // 

        if ((cnt / (double)cnt1) * 100 >= min_conf)
        {
            cout << "{";
            for (auto it : v1)
            {
                cout << it << ",";
            }
            cout << "} -> {";
            for (auto it : v2)
            {
                cout << it << ",";
            }
            cout << "} : " << (cnt / (double)cnt1) * 100 << "\n";
        }

        return;
    }

    v1.push_back(itemset[idx]);
    generateAssociationRule(itemset, idx + 1, v1, v2);

    v1.pop_back();
    v2.push_back(itemset[idx]);
    generateAssociationRule(itemset, idx + 1, v1, v2);
}

int main()
{

    ifstream fr("input2.csv", ios::in);

    if (!fr.is_open())
    {
        cout << "Error in opening file\n";
        return -1;
    }

    string line;

    set<string> items_coll;

    while (getline(fr, line))
    {

        stringstream str(line);

        string item;
        set<string> tr;

        while (getline(str, item, ','))
        {
            tr.insert(item); // Put item in transaction
            items_coll.insert(item);
        }

        trs.push_back(tr); // Put transaction in transactions vector
    }

    vector<string> items(items_coll.begin(), items_coll.end());

    generateItemSets(items, {}, 0); // Generate all possible itemsets and store in map

    int n = items.size();
    cout << "\nEnter Min Support : ";
    cin >> min_supp;

    cout << "\nEnter Min Confidence : ";
    cin >> min_conf;

    sc = ceil((min_supp / 100) * trs.size());
    cout << "\nSupport Count : " << sc << "\n";

    vector<vector<string>> freqIt;

    // Start by taking frequent itemsets of size 1,2,3 and so on till n
    for (int i = 1; i <= n; i++)
    {
        vector<vector<string>> fi = calcFreqItemSet(i); // Get frequent itemsets of size i

        if (fi.size() == 0)
        {
            cout << "No itemset of size : " << i << "\n";
            break;
        }

        cout << "Frequent itemset of size : " << i << " are : \n";

        // Print frequent - itemsets
        for (auto v : fi)
        {
            cout << "{";
            for (auto it : v)
            {
                cout << it << ",";
            }
            cout << "}\n";
        }

        freqIt = fi;
    }

    for (auto v : freqIt)
    {

        // For each itemset generate associative rules

        generateAssociationRule(v, 0, {}, {});
    }

    return 0;
}
