---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Nationwide Mortgage Licensing System and Registry Identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the number permanently assigned by the Nationwide Mortgage Licensing System and Registry (NMLS) for each company,
      branch, and individual that maintains a single account on NMLS.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: NMLSR ID
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://mortgage.nationwidelicensingsystem.org/about/Pages/NMLSID.aspx
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LicenseIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LicenseIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/NMLSR-ID
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: Nationwide Mortgage Licensing System and Registry Identifier
type: Ontology Class
---

# Nationwide Mortgage Licensing System and Registry Identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/NMLSR-ID>

## Definition

the number permanently assigned by the Nationwide Mortgage Licensing System and Registry (NMLS) for each company, branch, and individual that maintains a single account on NMLS.

## Relationships

- **Subclass of**: [LicenseIdentifier](/concepts/fibo/FND/Law/LegalCapacity/LicenseIdentifier.md)

## Annotations

- **label**: Nationwide Mortgage Licensing System and Registry Identifier
- **definition**: the number permanently assigned by the Nationwide Mortgage Licensing System and Registry (NMLS) for each company, branch, and individual that maintains a single account on NMLS.
- **abbreviation**: NMLSR ID
- **adaptedFrom**: http://mortgage.nationwidelicensingsystem.org/about/Pages/NMLSID.aspx

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
