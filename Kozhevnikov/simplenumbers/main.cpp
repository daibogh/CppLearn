#include <iostream>
#include <vector>
using namespace std;

void simplenums(int num, vector<int> &ptr)
{
	int k = 0;
	cout<<"test\n";
	for (int i = 2 ; i <= num ; ++i)
	{
		for (int j = 2 ; j < i ; ++j )
		{
			if (!(i%j))
				k++;
		}
		if (k)
			k = 0;
		else
		{
			// cout<<"test\n";
			ptr.push_back(i);
			// cout<<"test\n";
			// cout<<i<<endl;
		}
	}
}
void one_more_simple(int num,vector<int> &ptr)
{

	simplenums(num,ptr);
	int k = 0;
	while (1)
	{
		for (int j = 2 ; j < num ; ++j )
		{
			if (!(num%j))
				k++;
		}
		if (k)
		{
			k = 0;
			num++;
		}
		else
		{
			ptr.push_back(num);
			// cout<<num<<endl;	
			break;
		}
	}
}

int main(int argc, char const *argv[])
{
	vector<int> ptr;
	int num;
	cin >> num;
	simplenums(num,ptr);
	// one_more_simple(num,ptr.begin());

	for (int i = 0 ; i < ptr.size(); i++)
		cout<<ptr[i]<<endl;;
	return 0;
}