---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pass through m b s draft prospectus
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The draft prospectus for a pass through Mortgage Backed Securities issue, as determined by the issuing agency prior
      to marketing the issue. Certain terms in the draft prospectus will be finalized later in the issuance process to become
      the actual Prospectus. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSFinalProspectus
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/precedes
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSDraftProspectus
sources:
- id: fibo-source-2eeca2019d
  resource: references/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
  sha256: 2eeca2019d428c47ac1513eaf8db629142182da83295878f53a62e84592f6a59
  title: FIBO source BP/SecuritiesIssuance/AgencyMBSIssuance.rdf
title: pass through m b s draft prospectus
type: Ontology Class
---

# pass through m b s draft prospectus

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSDraftProspectus>

## Definition

The draft prospectus for a pass through Mortgage Backed Securities issue, as determined by the issuing agency prior to marketing the issue. Certain terms in the draft prospectus will be finalized later in the issuance process to become the actual Prospectus. Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [PreliminaryProspectus](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md)

## Constraints

- **[precedes](<https://www.omg.org/spec/Commons/DatesAndTimes/precedes>)**: some values from of type [PassThroughMBSFinalProspectus](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSFinalProspectus.md)

## Annotations

- **label** (en): pass through m b s draft prospectus
- **definition** (en): The draft prospectus for a pass through Mortgage Backed Securities issue, as determined by the issuing agency prior to marketing the issue. Certain terms in the draft prospectus will be finalized later in the issuance process to become the actual Prospectus. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
