---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has date specification
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: rule that specifies how a specified date is computed
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: The rule is modeled as a simple String because OWL2 provides no way to model the semantics of such a rule.
  domain:
  - concept: /concepts/fibo/FND/DatesAndTimes/FinancialDates/SpecifiedDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/SpecifiedDate
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasDateSpecification
sources:
- id: fibo-source-73e38ccf5b
  resource: references/fibo/FND/DatesAndTimes/FinancialDates.rdf
  sha256: 73e38ccf5b6081418aadb03212ccfec6d41de52fcce9c10aa5bc6533c41498b9
  title: FIBO source FND/DatesAndTimes/FinancialDates.rdf
title: has date specification
type: Ontology Property
---

# has date specification

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/hasDateSpecification>

## Definition

rule that specifies how a specified date is computed

## Relationships

- **Domain**: [SpecifiedDate](/concepts/fibo/FND/DatesAndTimes/FinancialDates/SpecifiedDate.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: has date specification
- **definition**: rule that specifies how a specified date is computed
- **editorialNote**: The rule is modeled as a simple String because OWL2 provides no way to model the semantics of such a rule.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
