import torch

import torch

# Check if CUDA is available
if torch.cuda.is_available():
    # Create a tensor on CPU
    x = torch.tensor([1, 2, 3])
    print("Tensor on CPU:")
    print(x)

    # Move the tensor to GPU
    x_cuda = x.cuda()
    print("\nTensor on CUDA-enabled GPU:")
    print(x_cuda)

    # Perform operations on GPU
    y_cuda = x_cuda * 2
    print("\nResult of operation on CUDA-enabled GPU:")
    print(y_cuda)
else:
    print("CUDA is not available. Cannot use .cuda() method.")

