---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial instrument identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters uniquely identifying a financial instrument for some purpose and within a specified context
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: Identifiers for financial instruments may include an ISIN, Sedol, CUSIP, BBGID, FIGI, or other identifier issued
      approximately when the instrument itself is issued, and based on the kind of instrument and jurisdiction in which it
      is issued.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: financial instrument identifier
type: Ontology Class
---

# financial instrument identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier>

## Definition

sequence of characters uniquely identifying a financial instrument for some purpose and within a specified context

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: min qualified cardinality 0 of type [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Annotations

- **label**: financial instrument identifier
- **definition**: sequence of characters uniquely identifying a financial instrument for some purpose and within a specified context
- **scopeNote**: Identifiers for financial instruments may include an ISIN, Sedol, CUSIP, BBGID, FIGI, or other identifier issued approximately when the instrument itself is issued, and based on the kind of instrument and jurisdiction in which it is issued.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
