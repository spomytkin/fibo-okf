---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mortgage indemnity insurance policy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: insurance policy providing the mortgage indemnity guarantee
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantee
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/InsurancePolicy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/InsurancePolicy
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityInsurancePolicy
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: mortgage indemnity insurance policy
type: Ontology Class
---

# mortgage indemnity insurance policy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityInsurancePolicy>

## Definition

insurance policy providing the mortgage indemnity guarantee

## Relationships

- **Subclass of**: [InsurancePolicy](/concepts/fibo/FBC/DebtAndEquities/Guaranty/InsurancePolicy.md)

## Constraints

- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: some values from of type [MortgageIndemnityGuarantee](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantee.md)

## Annotations

- **label** (en): mortgage indemnity insurance policy
- **definition** (en): insurance policy providing the mortgage indemnity guarantee

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
