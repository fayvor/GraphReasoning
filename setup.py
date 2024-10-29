from setuptools import setup, find_packages

# It's a good practice to read long descriptions outside the setup function
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='GraphReasoning',
    version='0.2.0',
    author='Markus J. Buehler',
    author_email='mbuehler@mit.edu',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'networkx',
        'matplotlib',
        'pandas',
        'transformers>=4.39',
        'powerlaw',
        'markdown2',
        'pdfkit',
        'bitsandbytes',
        'peft',
        'accelerate',
        'torch',
        'torchvision',
        'torchaudio',
        'huggingface_hub',
        'langchain',
        'langchain-community',
        'pyvis',
        'yachalk',
        'pytesseract',
        'llama-index',
        'llama-index-embeddings-huggingface',
        'tqdm',
        'ipython',
        'scikit-learn',
        'scipy',
        'seaborn',
        'uuid',
        'pdfminer.six',
        'guidance',
        'python-louvain',
        'wkhtmltopdf',
        'llama-cpp-python',
    ],
    description='GraphReasoning: Use LLM to reason over graphs, combined with multi-agent modeling.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lamm-mit/GraphReasoning',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.10',
)
