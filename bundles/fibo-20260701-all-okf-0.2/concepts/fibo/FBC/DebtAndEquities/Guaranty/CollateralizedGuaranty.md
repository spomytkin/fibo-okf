---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: collateralized guaranty
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: guaranty that takes the form of some asset that is pledged by a borrower to a lender (usually in return for a loan)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In some cases, the lender may require the borrower to place pledged assets such as cash or securities in a separate
      account that the lender controls.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/Guaranty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guaranty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/CollateralizedGuaranty
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: collateralized guaranty
type: Ontology Class
---

# collateralized guaranty

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/CollateralizedGuaranty>

## Definition

guaranty that takes the form of some asset that is pledged by a borrower to a lender (usually in return for a loan)

## Relationships

- **Subclass of**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guaranty.md)

## Constraints

- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: some values from of type [Collateral](/concepts/fibo/FBC/DebtAndEquities/Debt/Collateral.md)

## Annotations

- **label**: collateralized guaranty
- **definition**: guaranty that takes the form of some asset that is pledged by a borrower to a lender (usually in return for a loan)
- **explanatoryNote**: In some cases, the lender may require the borrower to place pledged assets such as cash or securities in a separate account that the lender controls.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
