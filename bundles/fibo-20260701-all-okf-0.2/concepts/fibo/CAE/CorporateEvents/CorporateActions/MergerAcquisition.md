---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: merger / acquisition
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporate action involving the consolidation of legal entities or assets
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Such consolidation may be accomplished via financial transactions such as mergers, acquisitions, consolidations,
      tender offers, purchase of assets, and management acquisitions.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MergerAcquisition
sources:
- id: fibo-source-54455443d7
  resource: references/fibo/CAE/CorporateEvents/CorporateActions.rdf
  sha256: 54455443d756001807a44fb86449f950a37301ed0646079052aa300d4b315193
  title: FIBO source CAE/CorporateEvents/CorporateActions.rdf
title: merger / acquisition
type: Ontology Class
---

# merger / acquisition

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/MergerAcquisition>

## Definition

corporate action involving the consolidation of legal entities or assets

## Relationships

- **Subclass of**: [MandatoryCorporateAction](/concepts/fibo/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)

## Annotations

- **label** (en): merger / acquisition
- **definition** (en): corporate action involving the consolidation of legal entities or assets
- **explanatoryNote** (en): Such consolidation may be accomplished via financial transactions such as mergers, acquisitions, consolidations, tender offers, purchase of assets, and management acquisitions.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
