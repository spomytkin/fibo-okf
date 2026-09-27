---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: global depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depositary receipt where a certificate issued by a depositary bank, which purchases securities of foreign companies,
      creates a security on a local exchange backed by those securities
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: GDR
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Global depositary receipts are the global equivalent of the original American depositary receipts (ADR) on which
      they are based. GDRs represent ownership of an underlying number of securities of a foreign company and are commonly
      used to invest in companies from developing or emerging markets by investors in developed markets.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: international depositary receipt
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: global depositary receipt
type: Ontology Class
---

# global depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt>

## Definition

depositary receipt where a certificate issued by a depositary bank, which purchases securities of foreign companies, creates a security on a local exchange backed by those securities

## Relationships

- **Subclass of**: [DepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md)

## Annotations

- **label** (en): global depositary receipt
- **definition** (en): depositary receipt where a certificate issued by a depositary bank, which purchases securities of foreign companies, creates a security on a local exchange backed by those securities
- **abbreviation** (en): GDR
- **explanatoryNote** (en): Global depositary receipts are the global equivalent of the original American depositary receipts (ADR) on which they are based. GDRs represent ownership of an underlying number of securities of a foreign company and are commonly used to invest in companies from developing or emerging markets by investors in developed markets.
- **synonym** (en): international depositary receipt

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
