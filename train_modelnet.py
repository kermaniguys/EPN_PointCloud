from ZPConvNets.trainer_modelnet import Trainer
from ZPConvNets.options import opt

if __name__ == '__main__':
    opt.model.flag = 'attention'
    opt.model.model = "cls_so3net_pn"

    if opt.mode == 'train':
        # overriding training parameters here
        opt.batch_size = 2
        opt.decay_rate = 0.5
        opt.decay_step = 20000
        opt.dropout_rate = 0.0
        opt.train_loss.attention_loss_type = 'default'

    trainer = Trainer(opt)
    if opt.mode == 'train':
        trainer.train()
    elif opt.mode == 'eval':
        trainer.eval() 