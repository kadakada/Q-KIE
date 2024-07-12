# Post Quantum Key-Independent Encryption

## Overview

Q-KIE introduces a novel post-quantum encryption technique based on a new hard problem, termed the Q-Problem. The Q-Problem offers a more complex and versatile variant of traditional computational problems, specifically addressing the challenges posed by quantum computing. The proposed Q-KIE scheme secures digital communications by hiding each communicating entity’s keys, with the encryption and decryption processes being performed based solely on the exchange of random private keys.
This innovative approach dynamically adjusts cryptographic hardness through parameterized complexity, ensuring a balanced combination of computational efficiency and robust security in both classical and post-quantum contexts. The adaptability and enhanced security of this scheme represent significant advancements in the field of quantum-resilient encryption.

## Features

- Resilience Against Post-Quantum Attacks: Q-KIE is designed to be secure against quantum computer attacks by avoiding number-theoretic problems such as factorization and discrete logarithms, which are vulnerable to Shor’s algorithm. This ensures that KIE remains secure even in the presence of advanced quantum computing capabilities.
- Low Complexity and Efficiency in Classical Computing: The classical implementation of KIE simplifies the key exchange process by not relying on the generation of large prime numbers or complex mathematical operations. This makes Q-KIE computationally efficient and practical for various applications.
- Implementation Feasibility: Q-KIE avoids matrices and other complex computations, ensuring that it can be implemented with lower computational overhead, which is particularly beneficial in resource-constrained environments.
-  Independent Key Advantages Based on Zero Information Sharing: One of the key advantages of Q-KIE is that it allows secure data exchange without the need for any information sharing between the communicating parties. This is achieved through the novel Q-problem, which ensures that each encryption operation uses different variables or expressions, enhancing security and eliminating key management issues.
- Robust Key Management: By not relying on shared or exchanged keys, Q-KIE simplifies key management and reduces the risk of key theft during communication. This is a significant advantage over traditional symmetric or asymmetric encryption methods that require key exchange mechanisms.

## Installation

To use the Q-KIE encryption technique, you need to have Python installed on your system and run the code.

