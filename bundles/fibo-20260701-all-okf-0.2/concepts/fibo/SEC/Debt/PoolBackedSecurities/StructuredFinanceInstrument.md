---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: structured finance instrument
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: pool-backed security wherein the risk associated with the pool has been uncoupled from the risk associated with
      the originating institution through a special purpose vehicle
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Collateralized debt obligations (CDOs), synthetic financial instruments, collateralized bond obligations (CBOs),
      and syndicated loans are examples of structured finance instruments.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Structured finance instruments represent a form of securitization technology which can be defined by three key
      characteristics: (1) pooling of financial assets, such as loans, bonds, or credit-default swaps; (2) de-linking of the
      credit risk of the asset pool from the credit risk of the originating firm, usually through use of a finite-lived, stand-alone
      special purpose vehicle (SPV); and (3) issuance by the SPV of "tranched" liabilities backed by the asset pool. Structured
      finance instruments are typically presented to large financial institutions or companies with complicated financing
      needs that are unsatisfied with conventional financial products.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: structured finance
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: Nf9bcec564b5d46568cc9fdc49d3e3608
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.bis.org/publ/cgfs23mitchell.pdf
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/StructuredProduct
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: structured finance instrument
type: Ontology Class
---

# structured finance instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument>

## Definition

pool-backed security wherein the risk associated with the pool has been uncoupled from the risk associated with the originating institution through a special purpose vehicle

## Relationships

- **See also**: [cgfs23mitchell.pdf](<https://www.bis.org/publ/cgfs23mitchell.pdf>)
- **Subclass of**: [StructuredProduct](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md)
- **Subclass of**: [PoolBackedSecurity](/concepts/fibo/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from value `Nf9bcec564b5d46568cc9fdc49d3e3608`

## Annotations

- **label** (en): structured finance instrument
- **definition** (en): pool-backed security wherein the risk associated with the pool has been uncoupled from the risk associated with the originating institution through a special purpose vehicle
- **example** (en): Collateralized debt obligations (CDOs), synthetic financial instruments, collateralized bond obligations (CBOs), and syndicated loans are examples of structured finance instruments.
- **explanatoryNote** (en): Structured finance instruments represent a form of securitization technology which can be defined by three key characteristics: (1) pooling of financial assets, such as loans, bonds, or credit-default swaps; (2) de-linking of the credit risk of the asset pool from the credit risk of the originating firm, usually through use of a finite-lived, stand-alone special purpose vehicle (SPV); and (3) issuance by the SPV of "tranched" liabilities backed by the asset pool. Structured finance instruments are typically presented to large financial institutions or companies with complicated financing needs that are unsatisfied with conventional financial products.
- **synonym** (en): structured finance

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
