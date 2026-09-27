---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: letter of credit guaranty
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: guaranty that takes the form of a letter of credit, i.e., a document issued by a bank guaranteeing the payment
      up to a stated amount for a specified period
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/LetterOfCredit
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isExemplifiedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/CollateralizedGuaranty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/CollateralizedGuaranty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/LetterOfCreditGuaranty
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: letter of credit guaranty
type: Ontology Class
---

# letter of credit guaranty

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/LetterOfCreditGuaranty>

## Definition

guaranty that takes the form of a letter of credit, i.e., a document issued by a bank guaranteeing the payment up to a stated amount for a specified period

## Relationships

- **Subclass of**: [CollateralizedGuaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty/CollateralizedGuaranty.md)

## Constraints

- **[isExemplifiedBy](/concepts/fibo/FND/Relations/Relations/isExemplifiedBy.md)**: some values from of type [LetterOfCredit](/concepts/fibo/FBC/DebtAndEquities/Guaranty/LetterOfCredit.md)

## Annotations

- **label**: letter of credit guaranty
- **definition**: guaranty that takes the form of a letter of credit, i.e., a document issued by a bank guaranteeing the payment up to a stated amount for a specified period

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
