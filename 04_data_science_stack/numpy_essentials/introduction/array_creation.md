**core NumPy array creation methods** 
Simple Hinglish. Real-life analogies.

---

## 1. `zeros()`

**Kya karta hai:**
Saare elements ko **0** se bhara hua array banata hai.

**Real life analogy:**
Socho ek **attendance sheet** jisme abhi kisi ka attendance mark nahi hua. Sab zero.

**Example:**

```python
import numpy as np
np.zeros(5)
```

**Output:**
`[0. 0. 0. 0. 0.]`

**Use case:**

* Counters
* Scores initialize karna
* Empty sensor readings

---

## 2. `ones()`

**Kya karta hai:**
Saare elements ko **1** se bhara hua array banata hai.

**Real life analogy:**
Ek **factory switchboard** jahan sab machines ON (1) state me hain.

**Example:**

```python
np.ones(4)
```

**Output:**
`[1. 1. 1. 1.]`

**Use case:**

* Default weights
* Flags
* Masking operations

---

## 3. `full()`

**Kya karta hai:**
Array jisme **har element same fixed value** hota hai (0 ya 1 zaroori nahi).

**Real life analogy:**
Class ke sab students ko **same bonus marks = 5** mile.

**Example:**

```python
np.full(6, 37)
```

**Output:**
`[37 37 37 37 37 37]`

**Use case:**

* Constant temperature assumption
* Default fill values
* Padding data

---

## 4. `arange()`

**Kya karta hai:**
Ek **sequence** banata hai, jaise Python `range()` but NumPy speed ke saath.

**Real life analogy:**
Train station ke **platform numbers**: 0, 1, 2, 3, 4…

**Example:**

```python
np.arange(0, 10, 2)
```

**Output:**
`[0 2 4 6 8]`

**Meaning:**
`start, stop, step`

**Use case:**

* Time steps
* Indexes
* Simulation loops

---

## 5. `eye()`

**Kya karta hai:**
**Identity matrix** banata hai
→ diagonal = 1, baaki sab = 0

**Real life analogy:**
School ke **result sheet** me sirf apna roll number apni row se match karta hai. Baaki sab mismatch (0).

**Example:**

```python
np.eye(4)
```

**Output:**

```
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

**Use case:**

* Linear algebra
* ML models
* Transformations
* Neutral element (like multiplying by 1)

---

## One-line mental model (important)

* `zeros` → **empty start**
* `ones` → **all active**
* `full` → **constant assumption**
* `arange` → **ordered sequence**
* `eye` → **self-mapping / identity**

If you understand these 5 properly, you already know **80% of NumPy array creation** used in real systems.
