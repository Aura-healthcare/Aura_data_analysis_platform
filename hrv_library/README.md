# Heart Rate Variability analysis library

**hrvanalysis** is a Python module for Heart Rate Variability Analysis built on top of SciPy, AstroPy, Nolds and NumPy and distributed under the GPLv3 license.

The development of this library started in July 2018 as part of Aura Healthcare project and is maintained by Robin Champseix.

Website : https://www.aura.healthcare/

version : 0.0.1


### Installion / Prerequisites

#### Dependencies

hrvanalysis requires the following:
- Python (>= 3.4)
- astropy = 3.0.4
- future = 0.16.0
- nolds = 0.4.1
- numpy = 1.15.1
- scipy = 1.1.0

#### User installation

The easiest way to install hrvanalysis is using ``pip`` :

    $ pip install -U hrvanalysis

you can also clone the repository:

    $ git clone https://github.com/robinchampseix/hrvanalysis.git
    $ python setup.py install

### Getting started 

There are 3 types of features you can get from NN Intervals: 

> Time domain features 

> Frequency domain features

> Non Linear domain features

As an exemple, what you can compute to get Time domain analysis is :

```python
from hrvanalysis import get_time_domain_features
nn_intervals = 
time_domain_features = get_time_domain_features(nn_intervals)
print(time_domain_features)

{'mean_nn': 718.248,
 'sdnn': 43.113074968427306,
 'sdsd': 19.519367520775713,
 'nn50': 24,
 'pnn50': 2.4,
 'nn20': 225,
 'pnn20': 22.5,
 'rmssd': 19.519400785039664,
 'Median_nn': 722.5,
 'Range_nn': 249}
```

You can find details and references about each feature in the documentation of each function:
- get_time_domain_features
- get_frequency_domain_features
- get_csi_cvi_features
- get_poincare_plot_features
- get_sampen

## References

Here are the main references used to compute the set of features:
- 
- 

## Authors

* **Robin Champseix** - *Initial work* - (https://github.com/robinchampseix)

## License

This project is licensed under the *GNU GENERAL PUBLIC License* - see the [LICENSE.md](https://github.com/robinchampseix/hrv_library/LICENSE) file for details

## Acknowledgments

* I hereby thank Laurent Ribière and Clément Le Couedic, my coworkers who gave me time to Open Source this library.
* I also thank Fabien Arcellier for his advices on to how build a library in PyPi.