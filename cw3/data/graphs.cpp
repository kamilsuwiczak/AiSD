#include <iostream>
#include <vector>
using namespace std;
class Graph {
private:
    int numVertices;
    vector<vector<int>> adjacencyMatrix;
    vector<vector<int>> successorList;
    vector<pair<int, int>> edgeList;
public:
    Graph(int vertices) {
        numVertices = vertices;
        adjacencyMatrix.resize(numVertices, vector<int>(numVertices, 0));
        successorList.resize(numVertices);
       
    }

    void addEdge(int source, int destination) {
        if (source >= 1 && source < numVertices && destination >= 1 && destination < numVertices) {
            
            adjacencyMatrix[source-1][destination-1] = 1;
            
            successorList[source-1].push_back(destination);
            edgeList.push_back(make_pair(source, destination));
        }
    }

    void printMatrix() {
        cout << " | ";
        for (int i = 0; i < numVertices; i++) {
            cout << i+1 << " ";
        }
        cout << endl;
        for (int i = 0; i < numVertices+1; i++) {
            cout << "==";
        }
        cout << endl;
        for (int i = 0; i < numVertices; i++) {
            cout << i+1 << "| ";
            for (int j = 0; j < numVertices; j++) {
                cout << adjacencyMatrix[i][j] << " ";
            }
            cout << endl;
        }
    }
    void printSuccessorList() {
        for (int i = 0; i < numVertices; i++) {
            cout << i+1 << ": ";
            for (int j = 0; j < successorList[i].size(); j++) {
                cout << successorList[i][j] << " ";
            }
            cout << endl;
        }
    }
    void printEdgeList() {
        for (int i = 0; i < edgeList.size(); i++) {
            cout << edgeList[i].first << " -> " << edgeList[i].second << endl;
        }
    }   
    
    
    
};   

int main() {
    Graph graph(5);

    graph.addEdge(1, 1);
    graph.addEdge(1, 2);
    graph.addEdge(2, 3);
    graph.addEdge(3, 4);
    graph.addEdge(4, 1);

    graph.printMatrix();
    graph.printSuccessorList();
    graph.printEdgeList();


    return 0;
}