function insersionSort(arr){
    startSort = 1
    while(startSort < arr.length){
        let currentValue = arr[startSort]
        let index = startSort
        while(index > 0 && currentValue < arr[index - 1]){
            arr[index] = arr[index - 1]
            index-=1;
        }
        arr[index] = currentValue
        startSort += 1
    }
}

const arr = [43, 24, 45, 27, 35, 47, 22, 48]

insersionSort(arr)

console.log(arr)
