function mat=isotropicMatrix(wavelength,sourcePoints,samplePoints)
% Compute the field induced by a collection of isotropic radiators
%
% function mat=isotropicMatrix(wavelength,sourcePoints,samplePoints)
%
% Input: wavelength   = operating wavelength (meters)
%        sourcePoints = location of point sources to solve (PxD, meters)
%        samplePoints = location of point where field is desired (SxD, meters)
% Output: mat = matrix that converts sources into samples (SxP)

% Wavenumber
k = 2*pi/wavelength;

% Sample points (NxP)
rangeVector=bsxfun(@minus,permute(samplePoints,[1 3 2]),permute(sourcePoints,[3 1 2]));
range=sqrt(sum(rangeVector.^2,3));

% Phase offsets (NxP) (dimensionless)
mat=exp(-sqrt(-1)*k.*range)./(4*pi*(eps+range));
mat(abs(range)<10*eps)=1; % Avoid divide-by-zero if source point overlaps sample point
