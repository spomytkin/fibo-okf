---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: exempt security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security that is exempt from certain regulatory rules
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Some exemptions from the registration requirement include: private offerings to a limited number of persons or
      institutions; offerings of limited size; intrastate offerings; and securities of municipal, state, and federal governments.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Securities Act of 1933
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Generally, securities must be filed with the appropriate regulatory agencies in the jurisdiction in which they
      are sold. The registration forms companies file provide essential facts while minimizing the burden and expense of complying
      with the law. Not all securities must be registered, however. By exempting many small offerings from the registration
      process, regulators seek to foster capital formation by lowering the cost of offering securities to the public.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/ExemptSecurity
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: exempt security
type: Ontology Class
---

# exempt security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/ExemptSecurity>

## Definition

security that is exempt from certain regulatory rules

## Relationships

- **Subclass of**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label**: exempt security
- **definition**: security that is exempt from certain regulatory rules
- **example**: Some exemptions from the registration requirement include: private offerings to a limited number of persons or institutions; offerings of limited size; intrastate offerings; and securities of municipal, state, and federal governments.
- **adaptedFrom**: Securities Act of 1933
- **explanatoryNote**: Generally, securities must be filed with the appropriate regulatory agencies in the jurisdiction in which they are sold. The registration forms companies file provide essential facts while minimizing the burden and expense of complying with the law. Not all securities must be registered, however. By exempting many small offerings from the registration process, regulators seek to foster capital formation by lowering the cost of offering securities to the public.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
