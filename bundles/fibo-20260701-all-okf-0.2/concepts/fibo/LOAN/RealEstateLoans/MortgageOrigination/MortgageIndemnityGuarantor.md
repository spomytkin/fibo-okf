---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mortgage indemnity guarantor
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: guarantor and insurer that provides mortgage insurance in the form of a mortgage indemnity guarantee (MIG)
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'SME Review notes 16 Sept: Guaranty - mortgage insurance e.g. insure up to 80% exposure. When you get into indemnification,
      then for instance if the product doesn''t meet the investor''s requirement such that if it doesn''t get paid then the
      lender steps in and takes the hit for the loan - this is usually a precondition for securitizing (issuing) the loan
      in a pool. If the loan is not going to be sold on the secondary market there would be no need to indemnify that loan
      so this term would not apply. Indemnification is insurance for the investor, while the lender is the one providing that
      indemnification.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/Insurer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Insurer
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: mortgage indemnity guarantor
type: Ontology Class
---

# mortgage indemnity guarantor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor>

## Definition

guarantor and insurer that provides mortgage insurance in the form of a mortgage indemnity guarantee (MIG)

## Relationships

- **Subclass of**: [Guarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md)
- **Subclass of**: [Insurer](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Insurer.md)

## Annotations

- **label** (en): mortgage indemnity guarantor
- **definition** (en): guarantor and insurer that provides mortgage insurance in the form of a mortgage indemnity guarantee (MIG)
- **explanatoryNote** (en): SME Review notes 16 Sept: Guaranty - mortgage insurance e.g. insure up to 80% exposure. When you get into indemnification, then for instance if the product doesn't meet the investor's requirement such that if it doesn't get paid then the lender steps in and takes the hit for the loan - this is usually a precondition for securitizing (issuing) the loan in a pool. If the loan is not going to be sold on the secondary market there would be no need to indemnify that loan so this term would not apply. Indemnification is insurance for the investor, while the lender is the one providing that indemnification.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
