#include <iostream>




int main() {
    int boardSideLength, rowForSumming;
    std::cin >> boardSideLength >> rowForSumming;
    int lastWhiteValue = boardSideLength % 2 == 0 ?
                         (boardSideLength * boardSideLength) / 2 :
                         (boardSideLength * boardSideLength) / 2 + 1;
    std::cout << "Max white: " << lastWhiteValue << std::endl;


    int maxWhiteRowValue = boardSideLength % 2 == 0 ?
                      (boardSideLength * rowForSumming) / 2 :
                      (rowForSumming % 2 != 0 ? (boardSideLength * rowForSumming) / 2  - rowForSumming / 2 :
                                                (boardSideLength * rowForSumming) / 2  + rowForSumming / 2 - 1);

    std::cout << "Max in row: " << maxWhiteRowValue << std::endl;

    return 0;
}
