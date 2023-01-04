pip install -r requirements.txt
python main.py --model resnet34 --optim sgd --lr 0.1 --momentum 0.9 --weight_decay 0.0005
python main.py --model resnet34 --optim sgd --lr 0.1 --momentum 0.9 --weight_decay 0.0005 --scheduler
python main.py --model resnet34 --optim adam --lr 1e-3 --eps 1e-8 --beta1 0.9 --beta2 0.999 --momentum 0.9
python main.py --model resnet34 --optim adabelief --lr 1e-3 --eps 1e-8 --beta1 0.9 --beta2 0.999 --momentum 0.9
python main.py --model resnet34 --optim acprop --lr 1e-3 --eps 1e-8 --beta1 0.9 --beta2 0.999 --momentum 0.9
python main.py --model resnet18 --optim sgd --lr 0.1 --momentum 0.9 --weight_decay 0.0005
python main.py --model resnet18 --optim sgd --lr 0.1 --momentum 0.9 --weight_decay 0.0005 --scheduler
python main.py --model resnet18 --optim adam --lr 1e-3 --eps 1e-8 --beta1 0.9 --beta2 0.999 --momentum 0.9
python main.py --model resnet18 --optim adabelief --lr 1e-3 --eps 1e-8 --beta1 0.9 --beta2 0.999 --momentum 0.9
python main.py --model resnet18 --optim acprop --lr 1e-3 --eps 1e-8 --beta1 0.9 --beta2 0.999 --momentum 0.9
python vis.py 