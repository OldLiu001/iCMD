from ipykernel.kernelapp import IPKernelApp

from .kernel import CMDKernel

IPKernelApp.launch_instance(kernel_class=CMDKernel)
