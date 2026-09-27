---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exempt issuer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: issuer that issues securities that are excused from certain regulatory reporting requirements
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: In general, these include governments and issuers of tax exempt securities such as municipalities, banks and depository
      institutions, and authorized insurance companies, railroads and public utilities, and certain non-profit organizations.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/exam-guide/series-66/regulation-of-securities/exempt-securities.asp
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ExemptIssuer
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: exempt issuer
type: Ontology Class
---

# exempt issuer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ExemptIssuer>

## Definition

issuer that issues securities that are excused from certain regulatory reporting requirements

## Relationships

- **Subclass of**: [Issuer](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)

## Annotations

- **label**: exempt issuer
- **definition**: issuer that issues securities that are excused from certain regulatory reporting requirements
- **example**: In general, these include governments and issuers of tax exempt securities such as municipalities, banks and depository institutions, and authorized insurance companies, railroads and public utilities, and certain non-profit organizations.
- **adaptedFrom**: http://www.investopedia.com/exam-guide/series-66/regulation-of-securities/exempt-securities.asp

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
