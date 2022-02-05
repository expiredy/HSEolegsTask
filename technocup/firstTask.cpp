#include <iostream>

int main() {
    int totalLoops, totalLoopIteration, activityKey;
    std::cin >> totalLoops;
    for (int index = 0; index < totalLoops; index++){
        std::cin >> totalLoopIteration;
        int previewDayActivity = 0, flowerTall = 1;
        for (int indexOf = 0; indexOf < totalLoopIteration; indexOf++){
            std::cin >> activityKey;
            if (flowerTall != -1) {
                if (previewDayActivity == 0 & activityKey == 0 & indexOf >= 1) {
                    flowerTall = -1;
                } else if (activityKey == 1) {
                    if (previewDayActivity == 1) {
                        flowerTall += 5;
                    } else if (previewDayActivity == 0) {
                        flowerTall += 1;
                    }

                }
                previewDayActivity = activityKey;
                }
            }
        std::cout << flowerTall << std::endl;
    }
    return 0;
}
