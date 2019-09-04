import numpy as np
import matplotlib.pyplot as plt
from ase.io import read, write

def get_RMSE(x_ref, x_pred):
    x_ref = np.array(x_ref)
    x_pred = np.array(x_pred)

    if np.shape(x_pred) != np.shape(x_ref):
        raise ValueError('WARNING: not matching shapes in rms')

    error_2 = (x_ref - x_pred) ** 2

    average = np.sqrt(np.average(error_2))
    return average

def plot_energy_force_error(dft_xyz, gap_xyz):
    """ Plots the distribution of energy per atom and each force component on the output vs the input"""

    # read files
    dft = read(dft_xyz, ':')
    gap = read(gap_xyz, ':')

    e_atom_dft = [at.info['energy'] / len(at) for at in dft]
    e_atom_gap = [at.info['energy'] / len(at) for at in gap]
    
    f_dft = np.array([at.arrays['forces'] for at in dft])
    f_gap = np.array([at.arrays['force'] for at in gap])
    
    Z_species = [1, 8, 78] # H, O, Pt   
    f_dft_all_Z = [np.vstack([f_dft[i][np.where(at.numbers == Z)] for i, at in enumerate(dft)]) for Z in Z_species]
    f_gap_all_Z = [np.vstack([f_gap[i][np.where(at.numbers == Z)] for i, at in enumerate(gap)]) for Z in Z_species]         
    
    # scatter plot of the data
    plt.figure(figsize=[14, 14])
    
    plt.subplot(221)
    plt.scatter(e_atom_dft, e_atom_gap, alpha=0.4)
    # get the appropriate limits for the plot
    emin = min(min(e_atom_dft), min(e_atom_gap))
    emax = max(max(e_atom_dft), max(e_atom_gap))
    de = emax - emin
    plt.xlim(emin, emax)
    plt.ylim(emin, emax)
    # add line of slope 1 for refrence
    plt.plot([emin, emax], [emin, emax], c='k', linestyle='dashed')
    # set labels
    plt.ylabel('Energy by GAP eV/atom')
    plt.xlabel('Energy by DFT eV/atom')
    plt.title('Energy')
    rmse = get_RMSE(e_atom_dft, e_atom_gap)
    rmse_text = 'RMSE:' + str(np.round(rmse* 1000, 2)  ) + ' meV/atom'
    plt.text(emin+0.1*de, emax-0.1*de, rmse_text, fontsize='20', horizontalalignment='left', verticalalignment='top')
    
    # scatter plot of the data
    for i, [f_dft_Z, f_gap_Z] in enumerate(zip(f_dft_all_Z, f_gap_all_Z)):
        plt.subplot(2, 2, 2+i)
        plt.scatter(np.ravel(f_dft_Z), np.ravel(f_gap_Z), alpha=0.4)
        fmax, fmin = max(np.ravel([f_dft_Z, f_gap_Z])), min(np.ravel([f_dft_Z, f_gap_Z]))
        plt.plot([fmin, fmax], [fmin, fmax], c='k', linestyle='dashed')
        df = fmax - fmin
        plt.xlim(fmin, fmax)
        plt.ylim(fmin, fmax)
        # set labels
        plt.ylabel('Force by GAP / $(eV/\AA)$')
        plt.xlabel('Force by DFT / $(eV/\AA)$')
        rmse = get_RMSE(np.ravel(f_dft_Z), np.ravel(f_gap_Z))
        rmse_text = 'RMSE:' + str(np.round(rmse, 3)) + ' $eV/\AA$'
        plt.text(fmin + 0.1 * df, fmax-0.1*df, rmse_text, fontsize='large', horizontalalignment='left', verticalalignment='top')
        plt.title(['H', 'O', 'Pt'][i])
    plt.show()