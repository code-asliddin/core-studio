#include <iostream>
#include <vector>
#include <string>

using namespace std;

void chizish() {
    // Shaxmat taxtasining boshlang'ich holati
        string taxta[8][8] = {
                {"R","N","B","Q","K","B","N","R"},
                        {"P","P","P","P","P","P","P","P"},
                                {".",".",".",".",".",".",".","."},
                                        {".",".",".",".",".",".",".","."},
                                                {".",".",".",".",".",".",".","."},
                                                        {".",".",".",".",".",".",".","."},
                                                                {"p","p","p","p","p","p","p","p"},
                                                                        {"r","n","b","q","k","b","n","r"}
                                                                            };

                                                                                cout << "\n  A B C D E F G H" << endl;
                                                                                    for(int i = 0; i < 8; i++) {
                                                                                            cout << 8-i << " ";
                                                                                                    for(int j = 0; j < 8; j++) {
                                                                                                                cout << taxta[i][j] << " ";
                                                                                                                        }
                                                                                                                                cout << 8-i << endl;
                                                                                                                                    }
                                                                                                                                        cout << "  A B C D E F G H\n" << endl;
                                                                                                                                        }

                                                                                                                                        int main() {
                                                                                                                                            cout << "--- Shaxmat O'yini ---" << endl;
                                                                                                                                                chizish();
                                                                                                                                                    return 0;
                                                                                                                                                    }
                                                                                                                                                    