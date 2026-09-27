---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: i p o preliminary prospectus
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/IPOFullProspectus
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/precedes
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/IPOPreliminaryProspectus
sources:
- id: fibo-source-fb4230f5b0
  resource: references/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance.rdf
  sha256: fb4230f5b0812f53d30ce91b5b00a7d962d30b713eb159867935983fd6f7bbe7
  title: FIBO source BP/SecuritiesIssuance/EquitiesIPOIssuance.rdf
title: i p o preliminary prospectus
type: Ontology Class
---

# i p o preliminary prospectus

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/IPOPreliminaryProspectus>

## Relationships

- **Subclass of**: [PreliminaryProspectus](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md)

## Constraints

- **[precedes](<https://www.omg.org/spec/Commons/DatesAndTimes/precedes>)**: some values from of type [IPOFullProspectus](/concepts/fibo/BP/SecuritiesIssuance/EquitiesIPOIssuance/IPOFullProspectus.md)

## Annotations

- **label** (en): i p o preliminary prospectus

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
