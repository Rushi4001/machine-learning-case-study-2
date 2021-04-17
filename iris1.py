from sklearn.datasets import load_iris

def main():
    dataset=load_iris()
    
    print("features of dataset")
    print(dataset.feature_names)

    print("target names of dataset")
    print(dataset.target_names)
    
    print("iris dataset is:")
    
    for icnt in range(len(dataset.target)):
        print("ID:%d feature : %s label : %s" %(icnt,dataset.data[icnt],dataset.target[icnt]))
    
if __name__ == "__main__":
    main()







