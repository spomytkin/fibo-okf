---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: promissory note
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt instrument that is a written promise by one party to another that commits that party to pay a specified sum
      on demand or within a specified time frame under specified terms
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Promissory notes are generally fully fungible. They may or may not be negotiable.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: promissory note
type: Ontology Class
---

# promissory note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote>

## Definition

debt instrument that is a written promise by one party to another that commits that party to pay a specified sum on demand or within a specified time frame under specified terms

## Relationships

- **Subclass of**: [DebtInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)

## Annotations

- **label**: promissory note
- **definition**: debt instrument that is a written promise by one party to another that commits that party to pay a specified sum on demand or within a specified time frame under specified terms
- **explanatoryNote**: Promissory notes are generally fully fungible. They may or may not be negotiable.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
