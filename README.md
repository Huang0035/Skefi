# SkeFi
SkeFi: Cross-Modal Knowledge Transfer for Wireless Skeleton-Based Action Recognition

# Requirement
Pytorch0 >= 0.4. (version 1.12.1 is used)

# Data Preparation
1. For Kinetics-Skeleton
 - Download the raw data from [Skeleton-Kinetics](https://github.com/yysijie/st-gcn). Then put them under the data directory:
 
        -data\  
          -kinetics_raw\  
            -kinetics_train\
              ...
            -kinetics_val\
              ...
            -kinetics_train_label.json
            -keintics_val_label.json

[https://github.com/yysijie/st-gcn]: Skeleton-Kinetics

 - Preprocess the data with

    `python data_gen/kinetics-gendata.py`

 - Generate the bone data with
    
    `python data_gen/gen_bone_data.py`

2. For MM-Fi
- Download the raw data from [MMFi_dataset](https://github.com/ybhbingo/MMFi_dataset), and follow the steps provided for data processing. You will end up with a series of .npz files.

- Preprocess the data with

    `python data_gen/MMFi_data_process.py`

- Generate the bone data with 
    
    `python data_gen/MMFi_gendata.py`

  And put them under the data directory.
 
# Training & Testing

Change the config file depending on what you want.

    `python main.py --config ./config/Transfer/train_joint.yaml`

If you want to do transfer learning, uncomment lines 250 to 257 in `main.py`.

# Contact
For any questions, feel free to contact `E220035@e.ntu.edu.sg` or `syhuang1025@gmail.com`
