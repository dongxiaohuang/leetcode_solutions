% # Counting Sort
% # the counting sort algorithm sort interger from a know range $k$ and it is a stable sort
void countingsort(int* array,int size, int k){
  int num[k+1]={0};
  int tmp[size];
  // for(int i = 0; i <= k; i++){num[i] = 0;}
  for(int i = 0; i < size; i++){
    num[array[i]] ++;
  }
  for(int i = 1; i <= k; i++){
    num[i] += num[i-1];
  }
  for(int i= size-1; i >= 0; i--){
    int index = num[array[i]];
    tmp[index] = array[i];
    num[array[i]]--;
  }
  for(int i = 0; i < size; i++){
    array[i] = tmp[i];
  }
}