---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mortgage
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: grant of financial interest in real property to a party that is not an owner of that real property and is recorded
      by a registration authority
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A mortgage prevents transfer of the ownership of the real property unless the financial interest is satisfied.
      Any loan can be collateralized by a mortgage, including, for example, a bail bond.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/SecurityAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/SecurityAgreement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/Mortgage
sources:
- id: fibo-source-69fec2eeb0
  resource: references/fibo/LOAN/RealEstateLoans/Mortgages.rdf
  sha256: 69fec2eeb0f7fc099e11c13a9ed3e6b5a1902c2f2a2af30a81282d1f4a6bdfa5
  title: FIBO source LOAN/RealEstateLoans/Mortgages.rdf
title: mortgage
type: Ontology Class
---

# mortgage

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/Mortgage>

## Definition

grant of financial interest in real property to a party that is not an owner of that real property and is recorded by a registration authority

## Relationships

- **Subclass of**: [SecurityAgreement](/concepts/fibo/FBC/DebtAndEquities/Debt/SecurityAgreement.md)

## Constraints

- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: some values from of type [RealProperty](/concepts/fibo/FND/Places/RealProperty/RealProperty.md)

## Annotations

- **label**: mortgage
- **definition**: grant of financial interest in real property to a party that is not an owner of that real property and is recorded by a registration authority
- **explanatoryNote** (en): A mortgage prevents transfer of the ownership of the real property unless the financial interest is satisfied. Any loan can be collateralized by a mortgage, including, for example, a bail bond.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
