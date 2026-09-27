---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exempt transaction
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: securities transaction for which there is no requirement to register the transaction with a regulatory agency
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include non-issuer transactions in outstanding securities, other isolated non-issuer transactions, certain
      unsolicited / de minimis transactions, fiduciary transactions, transactions with financial institutions, private placement
      transactions that meet certain conditions, and so forth.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/terms/e/exempttransaction.asp
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/SecuritiesTransaction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/SecuritiesTransaction
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ExemptTransaction
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: exempt transaction
type: Ontology Class
---

# exempt transaction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ExemptTransaction>

## Definition

securities transaction for which there is no requirement to register the transaction with a regulatory agency

## Relationships

- **Subclass of**: [SecuritiesTransaction](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/SecuritiesTransaction.md)

## Annotations

- **label**: exempt transaction
- **definition**: securities transaction for which there is no requirement to register the transaction with a regulatory agency
- **example**: Examples include non-issuer transactions in outstanding securities, other isolated non-issuer transactions, certain unsolicited / de minimis transactions, fiduciary transactions, transactions with financial institutions, private placement transactions that meet certain conditions, and so forth.
- **adaptedFrom**: http://www.investopedia.com/terms/e/exempttransaction.asp

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
