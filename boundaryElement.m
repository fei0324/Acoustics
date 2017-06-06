function sources=boundaryElement(wavelength,sourcePoints,dirichletPoints,desiredFields,neumannPoints,neumannNormals,desiredDerivs)
% Construct a solution for the scalar Helmholtz equation with mixed Dirichlet-Neumann 
% boundary conditions using the boundary element method
%
% function sources=boundaryElement(wavelength,sourcePoints,dirichletPoints,desiredFields,neumannPoints,neumannNormals,desiredDerivs)
%
% Input: wavelength      = operating wavelength (meters)
%        sourcePoints    = location of point sources to solve (PxD, meters)
%        dirichletPoints = locations of points where the field is specified (IxD, meters)
%        desiredFields   = the values of the field at each Dirichlet point (Ix1, field)
%        neumannPoints   = locations of points where normal derivatives are specified (NxD, meters)
%        neumannNormals  = normal vectors at each Neumann point (NxD, unit vector)
%        desiredDerivs   = the value of the derivative of the field at each Neumann point (Nx1, field/meter)
% Output: sources = values of each source (Px1)

% Wavenumber
k = 2*pi/wavelength;

% Which problems are active
dirichlet = exist('dirichletPoints','var') && ~isempty(dirichletPoints);
neumann = exist('neumannPoints','var' ) && ~isempty(neumannPoints);

%% Dirichlet subproblem
if dirichlet,
  % Construct Dirichlet submatrix via phases (IxP)
  dirichletMat=isotropicMatrix(wavelength,sourcePoints,dirichletPoints);
end

%% Neumann subproblem
if neumann,
  % Normalize supplied normal vectors (NxD)
  neumannNormals=bsxfun(@rdivide,neumannNormals,sqrt(sum(neumannNormals.^2,2)));

  % Construct vectors from each source point to each Neumann point  (NxPxD)
  neumannRangeVector=bsxfun(@minus,permute(neumannPoints,[1 3 2]),permute(sourcePoints,[3 1 2]));

  % Distance source to Neumann points (NxP)
  neumannRange=sqrt(sum(neumannRangeVector.^2,3));

  % Vectors source to Neumann, projected onto local normals (NxP)
  neumannProj=sum(bsxfun(@times,neumannRangeVector,permute(neumannNormals,[1 3 2])),3);

  % Construct Neumann submatrix (NxP)
  neumannMat=exp(-sqrt(-1)*k.*neumannRange)./(4*pi*(eps+neumannRange).^2).*neumannProj.*(1-1./neumannRange);
  neumannMat(abs(neumannRange)<10*eps)=0; % Avoid divide-by-zero if a source point overlaps a Neumann point
end

%% Combined problems

if dirichlet && neumann,
  sources = [dirichletMat ; neumannMat] \ [desiredFields ; desiredDerivs];
elseif dirichlet,
  sources = dirichletMat \ desiredFields;
elseif neumann,
  sources = neumannMat \ desiredDerivs;
end
