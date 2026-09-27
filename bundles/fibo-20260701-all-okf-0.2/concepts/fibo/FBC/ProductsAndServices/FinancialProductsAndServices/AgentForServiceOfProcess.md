---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: agent for service of process
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registered agent (person or organization) designated by a business entity, such as a corporation, to receive legal
      correspondence on behalf of the business entity in the jurisdiction in which the agent's address is located
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The person may be an officer of the corporation or a third party, such as the corporation's attorney, or a company
      providing such agency services.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.law.cornell.edu/wex/agent_for_service_of_process
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.sos.state.tx.us/corp/registeredagents.shtml
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/AgentForServiceOfProcess
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: agent for service of process
type: Ontology Class
---

# agent for service of process

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/AgentForServiceOfProcess>

## Definition

registered agent (person or organization) designated by a business entity, such as a corporation, to receive legal correspondence on behalf of the business entity in the jurisdiction in which the agent's address is located

## Relationships

- **See also**: [agent_for_service_of_process](<http://www.law.cornell.edu/wex/agent_for_service_of_process>)
- **See also**: [registeredagents.shtml](<http://www.sos.state.tx.us/corp/registeredagents.shtml>)
- **Subclass of**: [RegisteredAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md)

## Annotations

- **label**: agent for service of process
- **definition**: registered agent (person or organization) designated by a business entity, such as a corporation, to receive legal correspondence on behalf of the business entity in the jurisdiction in which the agent's address is located
- **explanatoryNote**: The person may be an officer of the corporation or a third party, such as the corporation's attorney, or a company providing such agency services.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
