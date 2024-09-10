# fine tune ProteinMPNN from a previous checkpoint,
# training only on tcr loop design data

# use_custom_design_mask flag allows the model to be trained on examples where lists of residues
# are specified for design, instead of one or more chains

python ../training/training.py \
    --path_for_outputs "output/version_2" \
    --path_for_training_data "training_data_v2/" \
    --previous_checkpoint "../vanilla_model_weights/v_48_020.pt" \
    --mixed_precision 0 \
    --num_examples_per_epoch 48 \
    --num_epochs 20 \
    --batch_size 1000 \
    --use_custom_design_mask 1 \
    --save_model_every_n_epochs 1
