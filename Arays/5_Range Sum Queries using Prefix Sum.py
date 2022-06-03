'''
Description : We are given an Array of n integers, We are given q queries having indices l and r . We have to find out sum between the given range of indices.
void fillPrefixSum(int arr[], int N, int prefixSum[])
    {
        prefixSum[0] = arr[0];

        // Adding present element
        // with previous element
        for (int i = 1; i < N; i++)
            prefixSum[i] = prefixSum[i-1] + arr[i];
    }

sumInRange = prefixSum[j]  , if i = 0

otherwise,

sumInRange = prefixSum[j] - prefixSum[i-1]  ,  if (i != 0).
'''