---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is submitted to
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the party to which something is submitted
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isSubmittedTo
sources:
- id: fibo-source-a52060e8b1
  resource: references/fibo/FND/Arrangements/Reporting.rdf
  sha256: a52060e8b187a3f08302027cf7c7be15c9b644d9a3a7105f69a6415913db5143
  title: FIBO source FND/Arrangements/Reporting.rdf
title: is submitted to
type: Ontology Property
---

# is submitted to

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isSubmittedTo>

## Definition

indicates the party to which something is submitted

## Relationships

- **Range**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)
- **Subproperty of**: [hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)

## Annotations

- **label**: is submitted to
- **definition**: indicates the party to which something is submitted

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
